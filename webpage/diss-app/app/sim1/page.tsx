
export default function Sim1() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        <div>
            <h1>World 1 Simulation</h1>
            <iframe
                src="http://localhost:1999"
                width="960"
                height="540"
                style={{ border: 'none' }}
            />
        </div>

        </main>
    </div>
  );
}
