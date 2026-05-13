const progressBar = document.getElementById("progressBar");
const progress = document.getElementById("progress");
const progressText = document.getElementById("progressText");

progressText.innerHTML = "0 seconds";
function startProgress() {
  duration = parseInt(timeInput.value);
  conssle.log("Input value:", duration);

  let elapsed = 0;
  setInterval(() => {
    elapsed++;
    const progress = (elapsed / duration) * 100;
    progressBar.style.width = `${progress}%`;

    if (progress >= 100) {
      clearInterval(interval);
    }
  }, 1000);
}

function resetProgress() {
  clearInterval(interval);
  progressBar.style.width = "2px";
  timeInput.value = "";
  progress.innerHTML = "0 seconds";
  elapsed = 0;
  duration = 0;
  interval = null;
}
