'use strict;';
var primeh1 = document.querySelector('#nextprime');
var numGenerated = 0;

function clickedon() {
  numGenerated++;
  let primes = Primes(numGenerated)
  let prime = primes.pop()
  primeh1.textContent = prime;
}

function Primes(n) {
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