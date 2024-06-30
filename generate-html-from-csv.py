import csv

def generate_html(csv_file, output_file):
    sections = {}
    current_section = None

    # Read the CSV file
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        # for row in reader:
        #     if len(row) == 1 and row[0]:  # Section header
        #         current_section = row[0]
        #         sections[current_section] = []
        #     elif len(row) == 2 and current_section:  # Item and price
        #         sections[current_section].append((row[0], row[1]))
        for row in reader:
            if len(row) == 1 and row[0]:  # Section header
                current_section = row[0]
                sections[current_section] = []
            elif len(row) == 2 and current_section:  # Item and price without category
                sections[current_section].append((row[0], row[1], None))
            elif len(row) == 3 and current_section:  # Item, price, and category
                sections[current_section].append((row[0], row[1], row[2]))

    # Generate HTML
    html_content = []
    html_content.append('<!--\n\nINIZIO CONTENUTO GENERATO\n\n-->')
   

    for section, items  in sections.items():
        
        html_content.append(f'<!--\n\nINIZIO SEZIONE: {section}\n\n-->')

        section_id = section.lower().replace(" ", "-")
        html_content.append(f'<section id="{section_id}" class="mb-16">')
        html_content.append('<div class="flex gap-2  items-end mb-10 ">')
        html_content.append(f'   <img src="icons/{section}.png" alt="Caffetterie" class="w-12 h-12 object-contain " />')
        html_content.append(f'  <h2 class="text-lg mx-2 font-bold font-serif tracking-widest uppercase    bg-sky-1200  w-full border-double  shadow-sky-400 border-b border-sky-300 pb-1 px-2">{section}</h2>')
        html_content.append('</div>')
        html_content.append('  <ul class="flex flex-col gap-y-2 px-4 text-sm">')

        curr_category = ""
        init_category = False

        for item, price, category in items:
            #print(category)
            #print((curr_category != category))

            if init_category and (curr_category != category):
                print(f"FINE con {item}")

                init_category = False
                curr_category = ""
                html_content.append(f'</ul>')


            if category and not init_category:
                print(f"NEW CATEGORY on {item}")

                init_category = True
                print(category)
                curr_category = category
                html_content.append(f'    <h4 class="text-sky-500 font-medium italic mb-1 mt-3"> {category} </h4>')
                html_content.append(f'    <ul class="flex flex-col gap-y-2  ml-2 mb-3">')
         
            
   

                

            html_content.append(f'    <li class="flex justify-between border-b border-gray-200 border-dashed py-1">')
            html_content.append(f'      <span class="max-w-[80%]">{item}</span><span>{price} €</span>')
            html_content.append(f'    </li>')

           

        
    
            

        html_content.append('  </ul>')
        html_content.append('</section>')

        html_content.append(f'<!--\n\nFINE SEZIONE: {section}\n\n-->')

    html_content.append('<!--\n\nFINE CONTENUTO GENERATO\n\n-->')
    

    # Write to output file
    with open(output_file, 'w') as outfile:
        outfile.write('\n'.join(html_content))

# Path to your CSV file and the output HTML file
csv_file = 'listino_prezzi.csv'
output_file = 'listino_prezzi.html'

# Generate the HTML
generate_html(csv_file, output_file)