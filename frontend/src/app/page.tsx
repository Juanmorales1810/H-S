import { Button } from "@/components/ui/button";
import { LogIn, UserRoundPlus } from "lucide-react";
import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <section className="flex flex-col justify-center items-center w-full h-screen max-w-5xl mx-auto">
      <h1 className="mb-8 text-2xl font-semibold">Landing Page</h1>
      <Image
        src="/next.svg"
        alt="Next.js Logo"
        width={300}
        height={300}
      />
      <div className="flex gap-6 my-8">
        <Button asChild variant="outline">
          <Link href="/auth/login">
            <LogIn size={16} />
            Iniciar Sesión
          </Link>
        </Button>
        <Button>
          <Link href="/auth/register" className="flex gap-2">
            <UserRoundPlus size={16} />
            Registrarse
          </Link>
        </Button>
      </div>
    </section>
  );
}
