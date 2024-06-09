import AddUser from "./add-user";
import Searchbar from "./searchbar";
import ProfilePicture from "./profile-picture";

export default function Sidebar() {
  return (
    <div>
      <div className="flex flex-row gap-x-4 p-4">
        <Searchbar />
        <AddUser />

      </div>
      <ProfilePicture name="Hurensohn" />
    </div>
  );
}
