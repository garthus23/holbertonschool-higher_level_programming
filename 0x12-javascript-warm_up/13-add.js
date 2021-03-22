#!/usr/bin/node

exports.add = function (num1, num2) {
  if ((num1 === undefined || !Number.isInteger(num1)) && (num2 === undefined || !Number.isInteger(num2))) {
    return 0;
  } else if (num2 === undefined || !Number.isInteger(num2)) {
    return num1;
  } else if (num1 === undefined || !Number.isInteger(num1)) {
    return num2;
  }
  if (Number.isInteger(num1) && Number.isInteger(num2)) {
    return (Number(num1) + Number(num2));
  } else {
    return 0;
  }
};
