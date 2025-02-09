document.addEventListener('DOMContentLoaded', function() {const links = document.querySelectorAll('header a');

  links.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();

      const targetId = this.getAttribute('href');
      const targetElement = document.querySelector(targetId);

      if (targetElement) {
        const offsetTop = targetElement.offsetTop - 100;

        window.scrollTo({
          top: offsetTop,
          behavior: 'smooth'
        });
      }
    });
  });
});


// Add event listeners to dropdown menus
document.addEventListener("DOMContentLoaded", function() {
  const dropdowns = document.querySelectorAll(".dropdown");

  dropdowns.forEach((dropdown) => {
    const dropdownContent = dropdown.querySelector(".dropdown-content");
    const dropdownButton = dropdown.querySelector(".dropbtn");

    dropdownButton.addEventListener("click", function() {
      dropdownContent.classList.toggle("show");
    });

    // Close the dropdown menu when clicking outside
    document.addEventListener("click", function(event) {
      if (!dropdown.contains(event.target)) {
        dropdownContent.classList.remove("show");
      }
    });
  });
});