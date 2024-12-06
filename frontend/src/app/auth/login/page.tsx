
'use client'

import { Form, FormControl, FormDescription, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form'
import { zodResolver } from '@hookform/resolvers/zod'
import { LoaderIcon, Eye, EyeOff } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { useToast } from "@/hooks/use-toast"
import { useRouter } from 'next/navigation'
import { useForm } from 'react-hook-form'
import { useState } from 'react'
import * as z from 'zod'

const formSchema = z.object({
    email: z.string().email({
        message: 'Por favor, introduce un correo electrónico válido.',
    }),
    password: z.string().min(6, {
        message: 'La contraseña debe tener al menos 6 caracteres.',
    }),
})

export default function Page() {
    const [isLoading, setIsLoading] = useState(false)
    const [showPassword, setShowPassword] = useState(false)
    const router = useRouter()
    const { toast } = useToast()

    const form = useForm<z.infer<typeof formSchema>>({
        resolver: zodResolver(formSchema),
        defaultValues: {
            email: '',
            password: '',
        },
    })

    async function onSubmit(values: z.infer<typeof formSchema>) {
        setIsLoading(true)

        try {
            // Aquí iría la lógica de autenticación
            console.log(values)

            // Simulamos una espera de 2 segundos
            await new Promise(resolve => setTimeout(resolve, 2000))

            toast({
                title: 'Inicio de sesión exitoso',
                description: 'Has iniciado sesión correctamente.',
            })

            router.push('/admin')
        } catch (error) {
            toast({
                title: 'Error',
                description: 'Hubo un problema al iniciar sesión. Por favor, inténtalo de nuevo.',
                variant: 'destructive',
            })
        } finally {
            setIsLoading(false)
        }
    }
    return (
        <section className='flex justify-center items-center w-full h-screen max-w-md mx-auto'>
            <Form {...form}>
                <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8 w-full bg-zinc-100 px-12 py-8 rounded-md shadow-md dark:bg-transparent dark:border-[1px] border-zinc-600">
                    <FormField
                        control={form.control}
                        name="email"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel className='font-semibold'>Correo electrónico</FormLabel>
                                <FormControl>
                                    <Input placeholder="tu@ejemplo.com" {...field} />
                                </FormControl>
                                <FormDescription className='text-xs'>
                                    Introduce tu dirección de correo electrónico.
                                </FormDescription>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                    <FormField
                        control={form.control}
                        name="password"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel className='font-semibold'>Contraseña</FormLabel>
                                <FormControl>
                                    <div className="relative">
                                        <Input
                                            type={showPassword ? "text" : "password"}
                                            placeholder="••••••"
                                            {...field}
                                        />
                                        <Button
                                            type="button"
                                            variant="ghost"
                                            size="sm"
                                            className="absolute right-0 top-0 h-full px-3 py-2 hover:bg-transparent"
                                            onClick={() => setShowPassword(!showPassword)}
                                        >
                                            {showPassword ? (
                                                <EyeOff className="h-4 w-4" aria-hidden="true" />
                                            ) : (
                                                <Eye className="h-4 w-4" aria-hidden="true" />
                                            )}
                                            <span className="sr-only">
                                                {showPassword ? 'Ocultar contraseña' : 'Mostrar contraseña'}
                                            </span>
                                        </Button>
                                    </div>
                                </FormControl>
                                <FormDescription className='text-xs'>
                                    Introduce tu contraseña.
                                </FormDescription>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                    <Button type="submit" disabled={isLoading}>
                        {
                            isLoading &&
                            <LoaderIcon size={16} className='mr-2 animate-spin' />
                        }
                        {isLoading ? 'Iniciando sesión...' : 'Iniciar sesión'}
                    </Button>
                </form>
            </Form>
        </section>
    )
}
