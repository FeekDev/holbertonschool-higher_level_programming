#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (string = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(string.repeat(this.width));
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const width = this.width;
    this.width = this.height;
    this.height = width;
  }
};
