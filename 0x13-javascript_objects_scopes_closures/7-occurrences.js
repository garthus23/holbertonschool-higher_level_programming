#!/usr/bin/node

exports.nbOccurences = function (list, char) {
  let i = 0;
  let result = 0;
  while (list[i]) {
    if (list[i] === char) {
      result++;
    }
    i++;
  }
  return result;
};
