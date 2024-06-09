import { Search } from "lucide-react";
import { Input } from "./ui/input";
import { useChatStore } from "./providers";

export default function Searchbar() {
  const setSearchFilter = useChatStore(state => state.setSearchFilter);
  const searchFilter = useChatStore(state => state.searchFilter);

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    setSearchFilter(e.target.value);
  }

  return <div className="relative ml-auto flex-1  w-full">
    <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
    <Input
      type="search"
      placeholder="Search..."
      value={searchFilter}
      onChange={handleChange}
      className="w-full rounded-lg bg-background pl-8 "
    />
  </div>
}
