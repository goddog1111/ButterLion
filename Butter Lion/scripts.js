document.addEventListener('DOMContentLoaded', function() {
    // District distribution data
    const districtData = {
        labels: ['Zhongzheng', 'Shilin', 'Da\'an', 'Datong', 'Zhongshan', 'Songshan', 'Wanhua', 'Neihu', 'Beitou', 'Nangang'],
        datasets: [{
            label: 'Number of Cleaning Bins',
            data: [259, 233, 224, 198, 195, 174, 153, 133, 97, 94],
            backgroundColor: [
                '#FEDAAF',
                '#FDFEBE',
                '#D0FEC6',
                '#ABC8FE',
                '#C4BBFE',
                '#FECCFE',
                '#FEDAAF',
                '#FDFEBE',
                '#D0FEC6',
                '#ABC8FE'
            ],
            borderColor: '#fff',
            borderWidth: 2
        }]
    };

    // Create district distribution chart
    const districtChart = new Chart(
        document.getElementById('districtChart'),
        {
            type: 'bar',
            data: districtData,
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Distribution of Cleaning Bins by District'
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Number of Bins'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'District'
                        }
                    }
                }
            }
        }
    );

    // Add smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Back to Top button logic
    const backToTopBtn = document.getElementById('backToTop');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTopBtn.style.display = 'block';
        } else {
            backToTopBtn.style.display = 'none';
        }
    });
    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}); 