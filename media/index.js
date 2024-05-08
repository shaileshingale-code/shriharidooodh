// line chart code
const xValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
const yValues = [24, 26, 20, 10, 20, 30, 21, 26, 29, 30, 12, 18];

new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
      fill: false,
      lineTension: 0,
      backgroundColor: "#f05c67",
      borderColor: "#f05c6726",
      data: yValues
    }]
  },
  options: {
    legend: { display: false },
    scales: {
      xAxes: [{
        scaleLabel: {
          display: true,
          labelString: 'Months' // Label for x-axis
        }
      }],
      yAxes: [{
        scaleLabel: {
          display: true,
          labelString: 'Attendance' // Label for y-axis
        },
        ticks: {
          min: 0,
          max: 30
        }
      }]
    }
  }
});


//chart ends


let menuicn = document.querySelector(".menuicn"); 
let nav = document.querySelector(".navcontainer"); 

menuicn.addEventListener("click", () => { 
	nav.classList.toggle("navclose"); 
})

let dropdown = document.querySelector(".dropdown");
let dropdownContent = dropdown.querySelector(".dropdown-content");

    dropdown.addEventListener("click", () => {
        // Toggle the dropdown content visibility
        dropdownContent.style.display = (dropdownContent.style.display === "none" || dropdownContent.style.display === "") ? "block" : "none";

        // Toggle the arrow direction
        dropdown.classList.toggle("open");
    });


