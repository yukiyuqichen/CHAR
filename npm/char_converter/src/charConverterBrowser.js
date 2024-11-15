import v2tData from './data/v2t.json' assert { type: 'json' };
import v2sData from './data/v2s.json' assert { type: 'json' };

class CharConverterBrowser {
    constructor(option, source = 'online') {
        if (option !== 'v2s' && option !== 'v2t') {
            throw new Error("Option must be either 'v2s' (simplified) or 'v2t' (traditional).");
        }
        this.mapping = {};
        this.mode = 'one2one';
        this.source = source; // 'online' or 'offline'

        // Return a promise that resolves when the mapping data is loaded
        this.loaded = this.loadMappingData(option);
    }

    async loadMappingData(option) {
        if (this.source === 'online') {
            const url = `https://yukiyuqichen.github.io/CHAR/char_converter/data/${option}.json`;
            try {
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                console.log("Online data loaded successfully.");
                const data = await response.json();
                this.mapping = data;
            } catch (error) {
                console.error("Error loading mapping data:", error);
            }
        } else if (this.source === 'offline') {
            try {
                if (option === 'v2s') {
                    this.mapping = v2sData;
                } else if (option === 'v2t') {
                    this.mapping = v2tData;
                } 
                console.log("Offline data loaded successfully.");
            } catch (error) {
                console.error("Error loading offline mapping data:", error);
            }
        } else {
            throw new Error("Invalid source. It must be either 'online' or 'offline'.");
        }
    }

    setMode(mode) {
        if (mode !== 'one2one' && mode !== 'one2many') {
            throw new Error("Mode must be either 'one2one' or 'one2many'.");
        }
        this.mode = mode;
        console.log(`Conversion mode is set to '${mode}'.`);
    }

    async convert(text) {
        // Ensure mapping data is loaded before converting
        await this.loaded;

        let convertedText = [];
        for (let char of text) {
            if (this.mode === 'one2one') {
                convertedText.push(this.mapping[char] ? this.mapping[char][0] : char);
            } else if (this.mode === 'one2many') {
                if (this.mapping[char] && this.mapping[char].length > 1) {
                    convertedText.push(`【${this.mapping[char].join('|')}】`);
                } else {
                    convertedText.push(this.mapping[char] ? this.mapping[char][0] : char);
                }
            }
        }
        return convertedText.join('');
    }
}

export default CharConverterBrowser;
