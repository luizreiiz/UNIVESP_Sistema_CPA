/* globals Chart:false */

(() => {
  "use strict";

  // Graphs
  const ctx = document.getElementById("myChart");
  // eslint-disable-next-line no-unused-vars
  const myChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: [
        "Domingo",
        "Segunda",
        "Terça",
        "Quarta",
        "Quinta",
        "Sexta",
        "Sábado",
      ],
      datasets: [
        {
          data: [15339, 21345, 18483, 24003, 23489, 24092, 22034],
          lineTension: 0,
          backgroundColor: "transparent",
          borderColor: "#ff9149",
          borderWidth: 4,
          pointBackgroundColor: "#f7f7f7",
        },
      ],
    },
    options: {
      plugins: {
        legend: {
          display: false,
        },
        tooltip: {
          boxPadding: 3,
        },
      },
    },
  });
})();
