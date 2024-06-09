'use client';
import { Plus } from 'lucide-react';
import { Button } from "./ui/button";
import { AddUserForm } from './add-user-form';

import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { useState } from 'react';

export default function AddUser() {
  const [open, setOpen] = useState(false);
  return (

    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>

        <Button>
          <Plus className="w-4 h-4" />
        </Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Add a new User</DialogTitle>
          <DialogDescription>
            Upload your WhatsApp conversation file to replicate your friends!
          </DialogDescription>
        </DialogHeader>

        <AddUserForm setOpen={setOpen} />

      </DialogContent>
    </Dialog>
  );
}
