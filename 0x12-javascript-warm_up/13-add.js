#!/usr/bin/node

exports.add = function (num1, num2) {
  if (num1 === undefined && num2 === undefined) {
      return 0;
  } else if (num2 === undefined) {
      return num1;
  } else if (num1 === undefined) {
      return num2;
  }
  if (parseInt(num1) && parseInt(num2)) {
    return (parseInt(num1) + parseInt(num2));
  }
};
