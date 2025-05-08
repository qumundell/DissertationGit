import Image from 'next/image';
import Link from 'next/link';

export default function main() {
    return (
      <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
        <title>Dissertation Front End</title>

            <h1 className="text-4xl sm:text-5xl font-bold text-center mb-1">
                The Simulations:
            </h1>

            <main className="flex flex-col row-start-2 items-center sm:items-start">
                <div className="flex gap-8 justify-center sm:justify-start w-full">
                    <div className="flex-shrink-0">
                        <Image src="/Dissertation_Pick_up_and_Place.jpg" alt="An image showing the thumbnail of the simulation" width={400} height={300} />
                        <Link href="/sim1" className="text-blue-500 hover:text-blue-700 font-medium text-xl">
                            Pick up and Place 
                        </Link>
                    </div>
                    <div className="flex-shrink-0">
                        <Image src="/vacuum_gripper.jpg" alt="An image showing the thumbnail of the simulation" width={400} height={300} />
                        <Link href="/sim2" className="text-blue-500 hover:text-blue-700 font-medium text-xl">
                            Carrying large objects
                        </Link>
                    </div>
                    <div className="flex-shrink-0">
                        <Image src="/Dissertation_Stirring_Tiago_Complete.jpg" alt="An image showing the thumbnail of the simulation" width={400} height={300} />
                        <Link href="/sim3" className="text-blue-500 hover:text-blue-700 font-medium text-xl">
                            Stirring a Pot
                        </Link>
                    </div>
                </div>
  
          </main>
      </div>
    );
  }
  