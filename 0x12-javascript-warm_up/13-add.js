#!/usr/bin/node

exports.add = function (num1, num2) {
  if (parseInt(num1) && parseInt(num2)) {
    return (parseInt(num1) + parseInt(num2));
  }
};
