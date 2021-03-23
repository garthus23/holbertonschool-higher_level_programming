#!/usr/bin/node
var convert10 = base10();
var convert16 = base16();

exports.converter = function (base) {
  if (parseInt(base) == 10) {
    return (convert10);
  } else if (parseInt(base) == 16) {
    return (convert16);
  }
};

exports.base10 = function (base) {
  return base;
};