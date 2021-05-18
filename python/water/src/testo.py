from h2o_wave import Q, ui, main, app


@app('/demo/nav')
async def serve2(q: Q):
    if '#' in q.args:
        hash_ = q.args['#']
        q.page['nav'] = ui.form_card(box='1 1 2 5', items=[
            ui.text(f'#={hash_}'),
            ui.button(name='show_nav', label='Back', primary=True),
        ])
    else:
        q.page['nav'] = ui.nav_card(
            box='1 1 2 5',
            value='#menu/spam',
            items=[
                ui.nav_group('Menu', items=[
                    ui.nav_item(name='#menu/spam', label='Spam'),
                    ui.nav_item(name='#menu/ham', label='Ham'),
                    ui.nav_item(name='#menu/eggs', label='Eggs'),
                    ui.nav_item(name='#menu/toast', label='Toast', disabled=True),
                ]),
                ui.nav_group('Help', items=[
                    ui.nav_item(name='#about', label='About', icon='Info'),
                    ui.nav_item(name='#support', label='Support', icon='Help'),
                ])
            ],
        )
    await q.page.save()


@app('/demo/theme')
async def serve1(q: Q):
    if not q.client.initialized:
        q.page['meta'] = ui.meta_card(box='')
        q.page['controls'] = ui.form_card(box='1 1 2 8', items=[
            ui.text_xl('Form'),
            ui.textbox(name='textbox', label='Textbox'),
            ui.toggle(name='toggle', label='Toggle'),
            ui.choice_group(name='choice_group', label='Choice group', choices=[
                ui.choice(name=x, label=x) for x in ['Egg', 'Bacon', 'Spam']
            ]),
            ui.checklist(name='checklist', label='Checklist', choices=[
                ui.choice(name=x, label=x) for x in ['Egg', 'Bacon', 'Spam']
            ]),
            ui.dropdown(name='dropdown', label='Dropdown', choices=[
                ui.choice(name=x, label=x) for x in ['Egg', 'Bacon', 'Spam']
            ]),
            ui.slider(name='slider', label='Slider'),
            ui.button(name='toggle_theme', label='Toggle Theme', primary=True)
        ])
        q.client.theme = 'default'
        q.client.initialized = True

    meta = q.page['meta']

    if q.args.toggle_theme:
        meta.theme = q.client.theme = 'neon' if q.client.theme == 'default' else 'default'

    await q.page.save()
