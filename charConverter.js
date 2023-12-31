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

    loadMappingData(option) {
        const url = `https://yukiyuqichen.github.io/CHAR/char_converter/data/${option}.json`; // Replace with your GitHub JSON URL
        return fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then(data => {
                this.mapping = data;
            })
            .catch(error => {
                console.error("Error loading mapping data:", error);
            });
    }

    setMode(mode) {
        if (mode !== 'one2one' && mode !== 'one2many') {
            throw new Error("Mode must be either 'one2one' or 'one2many'.");
        }
        this.mode = mode;
        console.log(`Conversion mode is set to '${mode}'.`);
    }

    convert(text) {
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

function initializeConverter() {
    const option = document.getElementById('optionSelect').value;
    const mode = document.getElementById('modeSelect').value;
    const converter = new CharConverter(option);
    converter.setMode(mode);
    return converter;
}

function convertFile() {
    const converter = initializeConverter();
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if (!file) {
        alert("Please select a file first.");
        return;
    }

    const reader = new FileReader();
    reader.onload = function(event) {
        const fileContent = event.target.result;
        converter.loaded.then(() => {
            const converted = converter.convert(fileContent);
            const blob = new Blob([converted], { type: 'text/plain;charset=utf-8' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'converted.txt';
            link.click();
        });
    };
    reader.readAsText(file, 'UTF-8');
}

function convertText() {
    const converter = initializeConverter();
    const inputText = document.getElementById('inputText').value;
    converter.loaded.then(() => {
        const converted = converter.convert(inputText);
        document.getElementById('outputText').value = converted;
    });
}
