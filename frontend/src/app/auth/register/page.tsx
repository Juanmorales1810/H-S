'use client'

import { Form, FormControl, FormDescription, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form'
import { Eye, EyeOff, LoaderIcon } from 'lucide-react'
import { zodResolver } from '@hookform/resolvers/zod'
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
    password: z.string().min(8, {
        message: 'La contraseña debe tener al menos 8 caracteres.',
    }),
    confirmPassword: z.string(),
}).refine((data) => data.password === data.confirmPassword, {
    message: "Las contraseñas no coinciden",
    path: ["confirmPassword"],
})

export default function Page() {
    const router = useRouter()
    const [isLoading, setIsLoading] = useState(false)
    const [showPassword, setShowPassword] = useState(false)
    const [showConfirmPassword, setShowConfirmPassword] = useState(false)
    const { toast } = useToast()

    const form = useForm<z.infer<typeof formSchema>>({
        resolver: zodResolver(formSchema),
        defaultValues: {
            email: '',
            password: '',
            confirmPassword: '',
        },
    })

    async function onSubmit(values: z.infer<typeof formSchema>) {
        setIsLoading(true)

        try {
            // Aquí iría la lógica de registro
            console.log(values)

            // Simulamos una espera de 2 segundos
            await new Promise(resolve => setTimeout(resolve, 2000))

            toast({
                title: 'Registro exitoso',
                description: 'Tu cuenta ha sido creada correctamente.',
            })

            router.push('/auth/login')
        } catch (error) {
            toast({
                title: 'Error',
                description: 'Hubo un problema al registrar tu cuenta. Por favor, inténtalo de nuevo.',
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
                                            placeholder="••••••••"
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
                                    Crea una contraseña segura de al menos 8 caracteres.
                                </FormDescription>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                    <FormField
                        control={form.control}
                        name="confirmPassword"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel className='font-semibold'>Confirmar contraseña</FormLabel>
                                <FormControl>
                                    <div className="relative">
                                        <Input
                                            type={showConfirmPassword ? "text" : "password"}
                                            placeholder="••••••••"
                                            {...field}
                                        />
                                        <Button
                                            type="button"
                                            variant="ghost"
                                            size="sm"
                                            className="absolute right-0 top-0 h-full px-3 py-2 hover:bg-transparent"
                                            onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                                        >
                                            {showConfirmPassword ? (
                                                <EyeOff className="h-4 w-4" aria-hidden="true" />
                                            ) : (
                                                <Eye className="h-4 w-4" aria-hidden="true" />
                                            )}
                                            <span className="sr-only">
                                                {showConfirmPassword ? 'Ocultar confirmación de contraseña' : 'Mostrar confirmación de contraseña'}
                                            </span>
                                        </Button>
                                    </div>
                                </FormControl>
                                <FormDescription className='text-xs'>
                                    Repite tu contraseña para confirmar.
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
                        {isLoading ? 'Registrando...' : 'Registrarse'}
                    </Button>
                </form>
            </Form>
        </section>
    )
}

