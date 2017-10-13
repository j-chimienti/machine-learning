




const wineQuality = require('../wineClassify');


const createIDX = ({_index, _type, _id}) => ({ "index" : { _index, _type,  _id } });



const arr = [];





wineQuality.forEach((w, idx) => {
  //arr.push(createIDX({_id: idx, _type: 'classify', _index: 'wine'}));

  arr.push(Object.assign({}, w, {id: idx}));
});


console.log(arr);

