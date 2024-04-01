const parentContainer =  document.querySelector('.cards-container');

parentContainer.addEventListener('click', event=>{

    const current = event.target;

    const isReadMoreBtn = current.className.includes('ler-mais-btn');

    if(!isReadMoreBtn) return;

    const currentText = event.target.parentNode.querySelector('.ler-mais-text');

    currentText.classList.toggle('ler-mais-text--show');

    current.textContent = current.textContent.includes('Ler mais') ? "Ler menos..." : "Ler mais...";

})