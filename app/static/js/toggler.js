document.addEventListener('DOMContentLoaded', () => {

  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Add a click event on each of them
  $navbarBurgers.forEach(el => {
    el.addEventListener('click', () => {

      // Get the target from the "data-target" attribute
      const target = el.dataset.target;
      const $target = document.getElementById(target);

      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      el.classList.toggle('is-active');
      $target.classList.toggle('is-active');

    });
  });

});

document.addEventListener('DOMContentLoaded', () => {
  (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
    const $notification = $delete.parentNode;

    $delete.addEventListener('click', () => {
      $notification.parentNode.removeChild($notification);
    });
  });
});


document.addEventListener('DOMContentLoaded', () => {
  const highlightWord = document.getElementById('highlight-word');

  const wordWidth = highlightWord.offsetWidth;
  const wordHeight = highlightWord.offsetHeight;

  const svgNS = "http://www.w3.org/2000/svg";

  const svg = document.createElementNS(svgNS, "svg");
  svg.setAttribute("width", wordWidth + 20); // Adjust as needed
  svg.setAttribute("height", wordHeight + 20); // Adjust as needed

  const path = document.createElementNS(svgNS, "path");
  path.setAttribute("d", `M10,${wordHeight / 2} Q50,10 ${wordWidth},${wordHeight / 2} T${wordWidth + 10},${wordHeight / 2}`);
  path.setAttribute("fill", "none");
  path.setAttribute("stroke", "blue");
  path.setAttribute("stroke-width", "2");
  path.setAttribute("stroke-dasharray", "4"); // Gives a hand-drawn dashed effect
  path.setAttribute("stroke-linecap", "round");

  svg.appendChild(path);
  highlightWord.appendChild(svg);
});
