"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"

import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"

const formSchema = z.object({
  username: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }),
  conversation: z.instanceof(File).refine((file) => file.size < 7000000, {
    message: 'Your file must be less than 7MB.',
  }),
})

export function AddUserForm({ setOpen }: { setOpen: any }) {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      username: "",
      conversation: undefined,
    },
  })

  function onSubmit(values: z.infer<typeof formSchema>) {
    values.conversation.text().then((text: string) => console.log(text));
    console.log(form)
    form.reset();
    setOpen(false);
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
        <FormField
          control={form.control}
          name="username"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Username</FormLabel>
              <FormControl>
                <Input placeholder="Tang Jie" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="conversation"
          render={({ field: { value, onChange, ...fieldProps } }) => (
            <FormItem>
              <FormLabel>Conversation Data (WhatsApp)</FormLabel>
              <FormControl>
                <Input
                  {...fieldProps}
                  placeholder="_chat.txt"
                  type="file"
                  accept=".txt"
                  onChange={(event) =>
                    onChange(event.target.files && event.target.files[0])
                  }

                />

              </FormControl>
            </FormItem>
          )}
        />
        <Button type="submit" >Submit</Button>
      </form>
    </Form>
  )
}
