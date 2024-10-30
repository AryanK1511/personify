import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent } from '@/components/ui/card';
import { Globe2 } from 'lucide-react';

interface URLInputFormProps {
    onLoadingChange: (loading: boolean) => void;
}

export const URLInputForm: React.FC<URLInputFormProps> = (props) => {
    const [url, setUrl] = useState('');

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        props.onLoadingChange(true);

        setTimeout(() => {
            console.log('Submitted URL:', url);
            props.onLoadingChange(false);
        }, 100000000);
    };

    return (
        <Card className="bg-black/50 backdrop-blur-md border-gray-800 rounded">
            <CardContent className="pt-6">
                <form onSubmit={handleSubmit} className="flex flex-col sm:flex-row gap-4">
                    <div className="relative flex-grow group">
                        <Globe2 className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 transition-colors group-focus-within:text-cyan-400" />
                        <Input
                            type="url"
                            placeholder="Enter website URL"
                            value={url}
                            onChange={(e) => setUrl(e.target.value)}
                            className="pl-10 bg-gray-900 border-gray-700 text-white placeholder-gray-500 focus:ring-cyan-400 focus:border-cyan-400 transition-all"
                            required
                        />
                    </div>
                    <Button
                        type="submit"
                        className="bg-gradient-to-r rounded from-purple-600 to-cyan-400 hover:from-purple-700 hover:to-cyan-500 text-white transition-all duration-300 ease-in-out transform hover:scale-105"
                    >
                        Generate Questions
                    </Button>
                </form>
            </CardContent>
        </Card>
    );
};
