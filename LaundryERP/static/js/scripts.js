document.addEventListener("DOMContentLoaded", () => {
  console.log("El DOM está listo.");
  const links = document.querySelectorAll(".hover-link");
  console.log("Número de enlaces encontrados:", links.length);

  links.forEach((link) => {
      link.addEventListener("mouseover", () => {
          link.style.backgroundColor = "orangered";
          link.style.color = "white";
      });

      link.addEventListener("mouseout", () => {
          link.style.backgroundColor = "";
          link.style.color = "";
      });
  });
});
    
