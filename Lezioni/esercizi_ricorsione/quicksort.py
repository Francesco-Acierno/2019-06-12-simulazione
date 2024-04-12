class QuickSort:
    def sort(self, sequenza):
        if len(sequenza) <= 1:
            return sequenza
        else:
            # 1) scegliere pivot
            pivot = sequenza[0]

            # 2) dividere la lista in sottoliste
            sequenza_smaller = []
            for i in range(1, len(sequenza)):
                if sequenza[i] < pivot:
                    sequenza_smaller.append(sequenza[i])

            sequenza_pivot = [n for n in sequenza if n == pivot]

            sequenza_large = [n for n in sequenza if n > pivot]

            # 3) fare il sort delle sottoliste e appendere i risultati
            return self.sort(sequenza_smaller) + self.sort(sequenza_pivot) + self.sort(sequenza_large)


if __name__ == '__main__':
    sequenza = [3, 5, 0, 2, 11, 31, 4, 7]
    print(f"La sequenza non ordinata : {sequenza}")
    print(f"La sequenza ordinata : {QuickSort().sort(sequenza)}")
