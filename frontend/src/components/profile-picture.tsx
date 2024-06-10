import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"

const stringToColour = (str: string) => {
  let hash = 0;
  str.split('').forEach(char => {
    hash = char.charCodeAt(0) + ((hash << 5) - hash)
  });
  let colour = '#';
  for (let i = 0; i < 3; i++) {
    const value = (hash >> (i * 8)) & 0xff;
    colour += value.toString(16).padStart(2, '0');
  }
  return colour;
}

interface PropsInterface {
  name: string;
}
export default function ProfilePicture({ name }: PropsInterface) {

  let colour = stringToColour(name);
  let hash = parseInt(colour.slice(1, colour.length), 16);
  let complementHash = hash ^ 0xffffff;
  let complement = '#' + complementHash.toString(16);

  return (
    <>
      <Avatar >
        <AvatarFallback style={{ backgroundColor: colour, color: complement }} className="font-bold">
          {name.slice(0, 1).toUpperCase()}
        </AvatarFallback>

      </Avatar>
    </>
  );
}
