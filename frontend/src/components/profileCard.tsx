'use client';
import ProfilePicture from "./profile-picture";
import { useChatStore } from "./providers";
import { cn } from "@/lib/utils";

interface Props {
  id: number;
  name: string;
}
export default function ProfileCard({ id, name }: Props) {
  const selected = useChatStore((state) => state.selected);
  const handleClick = useChatStore((state) => state.setSelected);

  return (
    <div className={cn("flex items-center p-2", { "bg-muted": selected == id })} onClick={() => handleClick(id)}>
      <ProfilePicture name={name} />
      <div className={cn("ml-2 text-lg", { "font-semibold": selected == id })}>
        {name}
      </div>
    </div>
  );
}
