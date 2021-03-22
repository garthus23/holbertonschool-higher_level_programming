#!/usr/bin/node

exports.callMeMoby = function (num, func) {
  let i;
  if (Number.isInteger(num)) {
    for (i = 0; i < num; i++) {
      func();
    }
  }
};
