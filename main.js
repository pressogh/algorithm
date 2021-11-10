const wait = (timeToDelay) => new Promise((resolve) => setTimeout(resolve, timeToDelay))

const h1 = async () => {
    console.log('H1');
    await wait(1000);
}

const h2 = async () => {
    await h1();
}

const h3 = async () => {
    await h1();
    console.log('H2');
}

h3();