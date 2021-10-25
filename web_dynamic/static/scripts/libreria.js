
export function createElement (type, attrList = {}, children = []) {
  const elem = document.createElement(type);
  const keys = Object.keys(attrList);
  keys.map(k => elem.setAttribute(k, attrList[k]));

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

export function appendRender (elem, DOMelem) {
  DOMelem.appendChild(elem);
  DOMelem.appendChild(elem);
}

export function Render (elem, DOMelem) {
  console.log(elem, DOMelem);
  DOMelem.appendChild(elem);
  DOMelem.appendChild(elem);
}
