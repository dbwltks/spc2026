for (let i = 2; i <= 9; i++) {
  for (let j = 1; j <= 9; j++) {
    console.log(`${i} X ${j} = ${i * j}`);
  }
  // console.log("--------------------------------");
}

function leftTriangle(n) {
  for (let i = 1; i <= n; i++) {
    console.log("*".repeat(i));
  }
}

leftTriangle(5);

function reverseLeftTriangle(n) {
  for (let i = n; i >= 1; i--) {
    console.log("*".repeat(i));
  }
}

reverseLeftTriangle(5);

function rightTriangle(n) {
  for (let i = 1; i <= n; i++) {
    console.log(" ".repeat(n - i) + "*".repeat(i));
  }
}

rightTriangle(5);

function reverseRightTriangle(n) {
  for (let i = n; i >= 1; i--) {
    console.log(" ".repeat(n - i) + "*".repeat(i));
  }
}

reverseRightTriangle(5);

function triangle(n) {
  for (let i = 1; i <= n; i++) {
    console.log("*".repeat(i));
  }
}

triangle(5);

function reverseTriangle(n) {
  for (let i = n; i >= 1; i--) {
    console.log(" ".repeat(n - i) + "*".repeat(i));
  }
}
