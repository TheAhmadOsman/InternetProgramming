'use strict;';

function isPrime(n) {
  let i = 2;
  while (i <= Math.sqrt(n)) {
    if (n % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}

function firstN(n) {
  const res = [];
  let i = 2;
  while (res.length < n) {
    if (isPrime(i)) {
      res.push(i);
    }
    i++;
  }
  return res;
}

function clickedon() {
  let np = document.querySelector('#numprimes');
  let plist = firstN(np.value);
  let mytable = document.querySelector('#primetab');
  mytable.innerHTML = '';
  for (let p of plist) {
    let tr = document.createElement('tr');
    let td = document.createElement('td');
    td.innerHTML = p;
    tr.appendChild(td);
    mytable.appendChild(tr);
  }
}