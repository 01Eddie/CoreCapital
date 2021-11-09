
function createElement (type, attrList = {}, children = [], content = '') {
  const elem = document.createElement(type);
  const keys = Object.keys(attrList);
  keys.map(k => elem.setAttribute(k, attrList[k]));
  elem.innerHTML = content;

  children.map(child => renderChild(elem, child));
  return elem;
}

function renderChild (elem, child) {
  if (typeof child === 'string') {
    elem.innerHTML += child;
    return;
  }
  elem.appendChild(child);
}

function appendRender (elem, DOMelem) {
  DOMelem.appendChild(elem);
}

// function render (elem, DOMelem) {
//   // console.log(elem, DOMelem);
//   DOMelem.innerHTML(elem);
// }
