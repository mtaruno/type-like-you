import { Search } from "lucide-react";
import { Input } from "./ui/input";

export default function Searchbar() {
  return <div className="relative ml-auto flex-1  w-full">
    <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
    <Input
      type="search"
      placeholder="Search..."
      className="w-full rounded-lg bg-background pl-8 "
    />
  </div>
}
