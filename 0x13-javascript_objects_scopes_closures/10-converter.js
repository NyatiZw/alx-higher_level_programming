#!/usr/bin/node

exports.converter = function (base) {
  return function convertToBase (number) {
    return number < base ? number.toString() : convertToBase(number / base | 0) + (number % base).toString();
  };
};
