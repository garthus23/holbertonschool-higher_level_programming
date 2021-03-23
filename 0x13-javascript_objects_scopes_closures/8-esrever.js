#!/usr/bin/node

exports.esrever = function (list) {
  let i = 0;

  while (list[i]) {
    i++;
  }
  i--;
  const newlist = [];
  let j = 0;
  while (i >= 0) {
    newlist[j] = list[i];
    i--;
    j++;
  }
  return (newlist);
};
