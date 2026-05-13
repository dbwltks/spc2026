const button1 = document.getElementById("incButton");
const button2 = document.getElementById("decButton");

button1.addEventListener(
  "click",
  () =>
    (document.getElementById("result").textContent =
      parseInt(result.textContent) + 1),
);

button2.addEventListener(
  "click",
  () =>
    (document.getElementById("result").textContent =
      parseInt(result.textContent) - 1),
);
