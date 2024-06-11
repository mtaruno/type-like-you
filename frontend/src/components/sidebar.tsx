'use client';
import AddUser from "./add-user";
import ProfileCard from "./profileCard";
import { useChatStore } from "./providers";
import Searchbar from "./searchbar";
import { fetchHistory } from "@/app/actions";
import { useQuery } from "@tanstack/react-query";

import Fuse from 'fuse.js'


export default function Sidebar() {

  const { data } = useQuery({ queryKey: ['history'], queryFn: fetchHistory });
  const searchFilter = useChatStore(state => state.searchFilter);

  let fuseResults = undefined;
  if (data && searchFilter != "") {
    const fuse = new Fuse(data, {
      keys: ['username']
    })
    fuseResults = fuse.search(searchFilter);
  }
  return (
    <div>
      <div className="flex flex-row gap-x-4 p-4">
        <Searchbar />
        <AddUser />
      </div>

      <div className="m-2 gap-x-2">
        {data && searchFilter == "" && data.map(({ username }, index) => (
          <ProfileCard name={username} id={index} key={username} />
        ))}

        {/* With Search Filter */}
        {fuseResults && fuseResults.map(({ item }, index) => (
          <ProfileCard name={item.username} key={item.username} id={index} />
        ))}
      </div>
    </div>
  );
}
