fetch('https://api.example.com/data')

    .then((response) => {

        if (response.ok) {

            return response.json();

        } else {

            throw new Error('Failed to fetch data');

        }

    })