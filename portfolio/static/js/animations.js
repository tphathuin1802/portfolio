// Animation configuration
const ANIMATION = {
  THRESHOLD: 0.1,
  ROOT_MARGIN: "0px",
};

// Animation observer
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        // Optional: Unobserve after animation
        // observer.unobserve(entry.target);
      }
    });
  },
  {
    threshold: ANIMATION.THRESHOLD,
    rootMargin: ANIMATION.ROOT_MARGIN,
  }
);

// Initialize animations
function initAnimations() {
  // Observe all sections
  document.querySelectorAll("section").forEach((section) => {
    observer.observe(section);
  });

  // Add animation classes to elements
  document.querySelectorAll(".btn").forEach((btn) => {
    btn.classList.add("scale-in");
  });

  // Add fade-in to specific elements
  document.querySelectorAll(".fade-in-element").forEach((element) => {
    element.classList.add("fade-in");
  });

  // Add slide-up to specific elements
  document.querySelectorAll(".slide-up-element").forEach((element) => {
    element.classList.add("slide-up");
  });
}

// Initialize when DOM is loaded
document.addEventListener("DOMContentLoaded", initAnimations);
