import { useEffect, useState } from 'react';
import { URLInputForm } from './components/URLInputForm/URLInputForm';
import LoadingScreen from './components/LoadingScreen/LoadingScreen';

const Home = () => {
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        const interval = setInterval(() => {
            document.documentElement.style.setProperty('--hue', Math.random() * 360 + 'deg');
        }, 3000);
        return () => clearInterval(interval);
    }, []);

    const handleLoading = (loading: boolean) => {
        setIsLoading(loading);
    };

    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-black text-white p-4 overflow-hidden">
            {isLoading ? (
                <LoadingScreen
                    heading="Generating Questions"
                    subHeading="Scraping the website, creating profiles and analyzing the data"
                />
            ) : (
                <div className="w-full max-w-md space-y-8 text-center relative z-10">
                    <h1 className="text-6xl font-extrabold tracking-tighter mb-4 animate-gradient-text">
                        Personify
                    </h1>
                    <p className="text-xl text-gray-300 mb-8 animate-fade-in-up">
                        Discover your web personality
                    </p>
                    <URLInputForm onLoadingChange={handleLoading} />
                </div>
            )}
            <footer className="mt-16 text-sm text-gray-400 animate-fade-in">
                © 2024 Personify. All rights reserved.
            </footer>
        </div>
    );
};

export default Home;
