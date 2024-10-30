import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

export function URLInputForm() {
    return (
        <div className="flex w-full max-w-sm items-center space-x-2">
            <Input type="text" placeholder="URL" />
            <Button type="submit">Generate Questions</Button>
        </div>
    );
}
