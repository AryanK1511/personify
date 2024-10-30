import React from 'react';
import { Loader2, Link, Computer, Briefcase, Globe, Code, BarChart } from 'lucide-react';

interface LoadingScreenProps {
    heading: string;
    subHeading: string;
}

const LoadingScreen: React.FC<LoadingScreenProps> = ({ heading, subHeading }) => {
    return (
        <div className="fixed inset-0 bg-black flex items-center justify-center">
            <div className="relative z-10 flex flex-col items-center justify-center space-y-6 mt-4">
                <div className="relative mb-10">
                    <div className="absolute inset-0 flex items-center justify-center animate-spin-slow">
                        <Link className="absolute text-purple-500 w-8 h-8 transform -translate-y-16" />
                        <Computer className="absolute text-cyan-500 w-8 h-8 transform translate-x-16" />
                        <Briefcase className="absolute text-purple-500 w-8 h-8 transform translate-y-16" />
                        <Globe className="absolute text-cyan-500 w-8 h-8 transform -translate-x-16" />
                        <Code className="absolute text-purple-500 w-8 h-8 transform translate-x-11 translate-y-11" />
                        <BarChart className="absolute text-cyan-500 w-8 h-8 transform -translate-x-11 -translate-y-11" />
                    </div>
                    <div className="relative z-10">
                        <div className="w-16 h-16 rounded-full bg-gradient-to-r from-purple-600 to-cyan-400 p-1">
                            <div className="w-full h-full rounded-full bg-black flex items-center justify-center">
                                <Loader2 className="w-8 h-8 text-white animate-spin" />
                            </div>
                        </div>
                    </div>
                </div>
                <div className="text-center mt-24">
                    <h2 className="text-4xl font-bold bg-gradient-to-r from-purple-400 to-cyan-400 text-transparent bg-clip-text animate-pulse">
                        {heading}
                    </h2>
                    <p className="text-gray-400 mt-2">{subHeading}</p>{' '}
                </div>
            </div>
        </div>
    );
};

export default LoadingScreen;
