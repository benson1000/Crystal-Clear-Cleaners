document.addEventListener('DOMContentLoaded', () => {
    const getQuoteLink = document.getElementById('getQuote');
    const quoteForm = document.getElementById('quoteForm');
    const closeFormButton = document.getElementById('closeForm');

    getQuoteLink.addEventListener('click', (event) => {
        event.preventDefault();
        quoteForm.style.display = 'block';
    });

    closeFormButton.addEventListener('click', () => {
        quoteForm.style.display = 'none';
    });
});
