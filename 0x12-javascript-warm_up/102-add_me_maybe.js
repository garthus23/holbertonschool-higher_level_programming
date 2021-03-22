#!/usr/bin/node

exports.addMeMaybe = function (num, func) {
  if (Number.isInteger(num)) {
    num++;
    func(num);
  }
};
