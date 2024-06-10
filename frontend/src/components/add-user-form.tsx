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
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import { toast } from "sonner"
import { useState } from "react"
import { useMutation } from "@tanstack/react-query"
import { uploadHistory } from "@/app/actions"

const formSchema = z.object({
  slang: z.string().optional(),
  conversation: z.instanceof(File).refine((file) => file.size < 7000000, {
    message: 'Your file must be less than 7MB.',
  }),
  other: z.string({ required_error: "You need to select a notification type." }),
});

export function AddUserForm({ setOpen }: { setOpen: any }) {

  const mutation = useMutation({
    mutationFn: uploadHistory,
    onSuccess: () => toast.success("Successfully uploaded data"),
    onError: () => toast.error("An error occurred while uploading..."),
  })

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      slang: "",
      conversation: undefined,
      other: undefined,
    },
  })
  const [names, setNames] = useState<string[] | null>(null);


  async function onSubmit(values: z.infer<typeof formSchema>) {
    const text = await values.conversation.text();
    const data = {
      whatsapp_name: values.other,
      whatsapp_history: text,
      user_slang_dictionary: values.slang ?? "",
    };
    console.log(data);
    mutation.mutate(data)
    form.reset();
    setOpen(false);
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
        <FormField
          control={form.control}
          name="slang"
          render={({ field }) => (
            <FormItem>
              <FormLabel>User Slang Dictionary</FormLabel>
              <FormControl>
                <Input placeholder="E.g. Mashallah: An expression used to indicate something good" {...field} />
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
                  onChange={(event) => {
                    if (event.target.files) {
                      event.target.files[0]
                        .text()
                        .then((text: string) => {
                          try {
                            //@ts-ignore
                            const names = [...new Set(text.match(/\] ([\w\s]+):/g).map(match => match.slice(2, -1)))];
                            setNames(names);
                          } catch {
                            setNames(null);
                          }
                        });
                    }
                    return onChange(event.target.files && event.target.files[0]);
                  }}
                />

              </FormControl>
            </FormItem>
          )}
        />

        {names && names.length != 2 && (
          <p>An error occurred while parsing the input file</p>
        )}
        {names && names.length == 2 && <FormField
          control={form.control}
          name="other"
          render={({ field }) => (
            <FormItem className="">
              <FormLabel>Who is the person you are texting with?</FormLabel>
              <FormControl>
                <RadioGroup
                  onValueChange={field.onChange}
                  defaultValue={field.value}
                  className="grid space-y-1 grid-cols-2"
                >
                  <FormItem className="flex items-center space-x-3 space-y-0">
                    <FormControl>
                      <RadioGroupItem value={names[0]} />
                    </FormControl>
                    <FormLabel className="font-normal">
                      {names[0]}
                    </FormLabel>
                  </FormItem>
                  <FormItem className="flex items-center space-x-3 space-y-0">
                    <FormControl>
                      <RadioGroupItem value={names[1]} />
                    </FormControl>
                    <FormLabel className="font-normal">
                      {names[1]}
                    </FormLabel>
                  </FormItem>
                </RadioGroup>
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        }
        <Button type="submit" >Submit</Button>
      </form>
    </Form>
  )
}
