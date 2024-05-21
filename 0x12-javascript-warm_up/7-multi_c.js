d#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log('Missing number of occurences');
} else {
  let i = 0;
  const max = process.argv[2];
  for (i; i < max; i++) {
    console.log('C is fun');
  }
}
