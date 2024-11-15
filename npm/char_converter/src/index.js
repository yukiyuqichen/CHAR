import CharConverterBrowser from './charConverterBrowser.js';
import CharConverterNode from './charConverterNode.js';

let CharConverter;

if (typeof window !== 'undefined') {
    console.log("Running in browser environment.");
    CharConverter = CharConverterBrowser;
} else {
    console.log("Running in Node.js environment.");
    CharConverter = CharConverterNode;
}

export default CharConverter;
