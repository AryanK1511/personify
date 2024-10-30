import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

export const URLInputForm: React.FC = () => {
    const [url, setURL] = useState<string | null>(null);

    const handleSubmit = () => {
        if (url) {
            console.log(`Generating questions for: ${url}`);
        }
    };

    return (
        <div className="flex w-full max-w-sm items-center space-x-2">
            <Input onChange={(e) => setURL(e.target.value)} type="text" placeholder="URL" />
            <Button type="button" onClick={handleSubmit} disabled={!url}>
                Generate Questions
            </Button>
        </div>
    );
};
