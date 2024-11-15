class CharConverter {
    constructor(option) {
        if (option !== 'v2s' && option !== 'v2t') {
            throw new Error("Option must be either 'v2s' (simplified) or 'v2t' (traditional).");
        }
        this.mapping = {};
        this.mode = 'one2one';

        // Return a promise that resolves when the mapping data is loaded
        this.loaded = this.loadMappingData(option);
    }

    async loadMappingData(option) {
        const url = `https://yukiyuqichen.github.io/CHAR/char_converter/data/${option}.json`; // Replace with your GitHub JSON URL
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            const data = await response.json();
            this.mapping = data;
        } catch (error) {
            console.error("Error loading mapping data:", error);
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

module.exports = CharConverter;
